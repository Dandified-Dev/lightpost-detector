<!-- <script lang="ts">
    // 1. This finds all .jpg, .jpeg, and .png files inside /static/dataset/
    //    The 'eager: true' part loads them all immediately.
    const allImageFiles = import.meta.glob('/static/dataset/**/*.{jpg,jpeg,png}', { eager: true });

    // 2. This function cleans up the file path to be a usable URL
    function getImageUrl(path: string): string {
        // The path from glob will be '/static/dataset/download.jpg'
        // We need to remove '/static' to make a valid URL
        return path.replace('/static', '');
    }

    // 3. Create a clean array of just the image URLs
    let images: string[] = Object.keys(allImageFiles).map(getImageUrl);
    images = images.slice(0, 10); // Limit to first 100 images for performance

    // images will now be:
    // [
    //   "/dataset/download.jpg",
    //   "/dataset/test/test_image_1.jpg",
    //   "/dataset/test/test_image_2.jpg",
    //   "/dataset/train/train_image_1.jpg"
    // ]
</script>

<div class="flex flex-1 flex-col gap-4 p-4">
    <div class="grid auto-rows-min gap-4 md:grid-cols-3">
        <div class="bg-muted/50 aspect-video rounded-xl cursor-pointer">
            <blockquote>
                adasd
            </blockquote>
            Total Test images: {images.length}
        </div>
    </div>
    <div class="grid auto-rows-min gap-4 md:grid-cols-5">
      {#each images as imageUrl}
          <div class="bg-muted/50 aspect-square rounded-xl">
              <img src={imageUrl} alt="Training data" class="h-full w-full object-cover rounded-xl" loading="lazy"/>
          </div>
      {/each}
    </div>
</div> -->