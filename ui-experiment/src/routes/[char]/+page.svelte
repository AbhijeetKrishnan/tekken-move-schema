<script lang="ts">
	import FrameDataDisplay from '../../components/FrameDataDisplay.svelte';
	export let data;
</script>

<main>
	<h1>CSV Table Viewer</h1>
	<FrameDataDisplay {data} />
</main>