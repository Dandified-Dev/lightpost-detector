<script lang="ts">
  import * as Empty from "$lib/components/ui/empty/index.js";
  import { IconCloud as CloudIcon } from '@tabler/icons-svelte';
  import { Input } from "$lib/components/ui/input/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Separator } from "$lib/components/ui/separator/index.js";
  import { Slider } from "$lib/components/ui/slider/index.js";

  let value = $state(33);
  let files = $state<FileList | undefined>();
  let processedImageUrl = $state<string | null>(null);

  async function uploadFiles() {
    const selectedFiles = files;

    if (!selectedFiles || selectedFiles.length === 0) return;

    const file = selectedFiles[0]; // only one file
    const formData = new FormData();
    formData.append('image', file); // matches backend parameter name

    try {
      const response = await fetch(`http://127.0.0.1:8000/api/process-image?confidence=${value / 100}`, {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Get image as blob
      const blob = await response.blob();
      const imageUrl = URL.createObjectURL(blob);

      processedImageUrl = imageUrl;

    } catch (err) {
      console.error('Upload failed:', err);
    }
  }


  $effect(() => {
    if (files) {
      uploadFiles();
    }
  });


</script>

<div class="flex flex-col gap-8 h-full">
  <div class="flex justify-between">
    <Button class="cursor-pointer" variant="destructive" onclick={() => files = undefined}>Clear</Button>
    <div class="flex gap-2 w-fit items-center">
      <Slider class="w-28" type="single" bind:value max={100} step={1} />
      <p>Confidence threshold: {value}</p>
    </div>
  </div>
  <Separator />
  {#if !files || files.length === 0}
  <Empty.Root class="border border-dashed h-full">
    <Empty.Header>
     <Empty.Media variant="icon">
      <CloudIcon />
     </Empty.Media>
     <Empty.Title>No Images</Empty.Title>
     <Empty.Description>
      Upload an image to get started.
     </Empty.Description>
    </Empty.Header>
    <Empty.Content>
     <Input bind:files={files} on:change={(e) => uploadFiles()} id="picture" type="file" accept="image/*"/>
    </Empty.Content>
  </Empty.Root>
  {:else if processedImageUrl}
    <div class="flex flex-col items-center justify-center md:h-[50%]">
      <div class="bg-muted/50 rounded-xl overflow-hidden">
        <img
          src={processedImageUrl}
          alt="Processed Image"
          class="h-full md:h-[800px] w-full object-cover"          
          />
      </div>
    </div>
  {/if}
</div>