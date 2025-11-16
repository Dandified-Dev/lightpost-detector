<script lang="ts">
	import '../app.css';
 	let { children } = $props();
	import AppSidebar from "$lib/components/app-sidebar.svelte";
  	import { Separator } from "$lib/components/ui/separator/index.js";
  	import * as Sidebar from "$lib/components/ui/sidebar/index.js";
</script>
 

 <main>
	<Sidebar.Provider>
	  <!-- <AppSidebar /> -->
	  <Sidebar.Inset>
	    <!-- <header class="flex h-16 shrink-0 items-center gap-2 border-b">
	      <div class="flex items-center gap-2 px-3">
	        <Sidebar.Trigger />
	        <Separator orientation="vertical" class="mr-2 h-4" />
	      </div>
	    </header> -->
		<div class="p-12 h-full">		
			{@render children?.()}
		</div>
	  </Sidebar.Inset>
	</Sidebar.Provider>
 </main>
