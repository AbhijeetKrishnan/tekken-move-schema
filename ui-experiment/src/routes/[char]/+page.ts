import { error } from '@sveltejs/kit';
import type { CsvData } from '../../types/csvData.type.js';

import Papa from 'papaparse';

export async function load({ fetch, params }) {
	const response = await fetch(`/frame-data/${params.char}.csv`);
	if (response.ok) {
		const data = await response.text();

		const result = Papa.parse(data, {
			header: true,
			dynamicTyping: true
		});

		const csvHeader = result.meta.fields;
		const csvData = result.data as object[];

		return {
			csvData: csvData,
			csvHeader: csvHeader
		} as CsvData;
	} else {
		throw error(response.status, 'Not found');
	}
}
