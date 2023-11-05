<script lang="ts">
	export let header: string[];

    const columnsToHide = [
        'id',
        'parent',
        'notes',
    ];
</script>

<div class="headerRow">
	{#each header as column}
        {#if !columnsToHide.includes(column)}
		    <div class={column}>{column}</div>
        {/if}
	{/each}
</div>

<style>
    .headerRow {
        display: flex;
        flex-direction: row;
        padding: 0.5rem;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-weight: bold;
    }
    .headerRow > div {
        flex: 1;
    }
    .headerRow > .name {
        flex: 2;
        text-align: left;
    }
    .headerRow > .input {
        flex: 3;
    }
    .headerRow > .damage {
        flex: 1;
    }
    .headerRow > .target {
        flex: 1;
    }
    .headerRow > .reach {
        flex: 1;
    }
    .headerRow > .tracksLeft {
        flex: 1;
    }
    .headerRow > .tracksRight {
        flex: 1;
    }
    .headerRow > .startup {
        flex: 1;
    }
    .headerRow > .recv {
        flex: 1;
    }
    .headerRow > .block {
        flex: 1;
    }
    .headerRow > .hit {
        flex: 1;
    }
    .headerRow > .ch {
        flex: 1;
    }
    .headerRow > .notes {
        flex: 3;
    }
</style>