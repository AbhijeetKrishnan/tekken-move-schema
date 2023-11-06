<script lang="ts">
	import { characters } from '../components/Characters.svelte';
</script>

<div class="container mx-auto my-auto h-screen w-screen">
	<h1 class="font-serif text-3xl font-bold underline text-center pb-14">Characters</h1>

	<div class="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-5  gap-x-0 gap-y-4 justify-center place-items-center">
		{#each Object.entries(characters) as [char_key, char_name]}
			<a href="/{char_key}">
				<div
					class="flex flex-col items-center justify-center rounded-lg shadow-lg hover:shadow-xl hover:bg-red-100"
				>
					<div class="p-2">
						<img
							class="rounded-full object-fill border-red-900 border-2"
							src="/t7_char_icons/{char_key}.png"
							alt="Character icon"
						/>
					</div>
					<div class="font-serif text-base font-bold hover:underline pb-2">
						<a href="/{char_key}">
							{char_name}
						</a>
					</div>
				</div>
			</a>
		{/each}
	</div>
</div>
