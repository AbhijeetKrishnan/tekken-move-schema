<script lang="ts">
	import FrameDataDisplay from '../../components/FrameDataDisplay.svelte';
	import { characters } from '../../components/Characters.svelte';
	import type { CsvData } from '../../types/csvData.type';

	export let data: CsvData;
	let charName = characters[data.character];
</script>

<main>
	<h1>{charName} Frame Data</h1>
	<FrameDataDisplay {data} />
</main>
