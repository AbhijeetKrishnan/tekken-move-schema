<script lang="ts">
	import type { CsvData } from '../types/csvData.type';
	import RowDisplay from './RowDisplay.svelte';
	import HeaderRowDisplay from './HeaderRowDisplay.svelte';

	export let data: CsvData;
</script>

{#if data && data.csvData && data.csvHeader}
	<HeaderRowDisplay header={data.csvHeader} />
	{#each data.csvData.entries() as [index, row]}
		<RowDisplay {index} {row} />
	{/each}
{/if}
