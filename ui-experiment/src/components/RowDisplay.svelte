<script lang="ts">
	import type { Move } from '../types/move.type';

	export let index: number;
	export let row: Move;

	const columnsToHide = ['id', 'parent', 'notes'];
</script>

<div class="row {index % 2 === 0 ? 'even' : 'odd'}">
	{#each Object.entries(row) as [key, value]}
		{#if !columnsToHide.includes(key)}
			<div class={key}>{value}</div>
		{/if}
	{/each}
</div>

<style>
	.row {
		display: flex;
		flex-direction: row;
		padding: 0.5rem;
		align-items: center;
		justify-content: center;
		text-align: center;
	}
	.odd {
		background-color: #eee;
	}
	.row > div {
		flex: 1;
	}
	.row > .name {
		flex: 2;
		width: 3vw;
		text-align: left;
	}
	.row > .input {
		flex: 3;
		width: 1vw;
	}
	.row > .damage {
		flex: 1;
	}
	.row > .target {
		flex: 1;
	}
	.row > .reach {
		flex: 1;
	}
	.row > .tracksLeft {
		flex: 1;
	}
	.row > .tracksRight {
		flex: 1;
	}
	.row > .startup {
		flex: 1;
	}
	.row > .recv {
		flex: 1;
	}
	.row > .block {
		flex: 1;
	}
	.row > .hit {
		flex: 1;
	}
	.row > .ch {
		flex: 1;
	}
	.row > .notes {
		flex: 3;
	}
</style>
