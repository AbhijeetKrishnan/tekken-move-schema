<script lang="ts">
	import type { CsvData } from '../types/csvData.type';

	export let data: CsvData;
</script>

{#if data && data.csvData && data.csvHeader}
	<table>
		<tr>
			{#each data.csvHeader as header}
				<th>{header}</th>
			{/each}
		</tr>
		{#each data.csvData as row, index}
			<tr class={index % 2 === 0 ? 'even' : 'odd'}>
				{#each Object.values(row) as value}
					<td>{value}</td>
				{/each}
			</tr>
		{/each}
	</table>
{/if}
