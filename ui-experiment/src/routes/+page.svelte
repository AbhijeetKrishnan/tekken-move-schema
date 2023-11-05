<script lang="ts">
	import { characters } from '../components/Characters.svelte';
</script>

<h1>Characters</h1>
<ol>
	{#each Object.entries(characters) as [char_key, char_name]}
		<li><a href="/{char_key}">{char_name}</a></li>
	{/each}
</ol>
