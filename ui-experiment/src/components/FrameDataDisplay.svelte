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

<style>
	/* Base styles for the table cells */
	table {
		border-collapse: collapse;
		width: 100%;
	}

	th,
	td {
		border: 1px solid #aaa;
		padding: 8px;
		text-align: left;
	}

	th {
		background-color: #70707075;
	}

	tr:nth-child(even) {
		background-color: #f2f2f2;
	}

	tr:nth-child(odd) {
		background-color: #ffffff;
	}
</style>
