import type { Move } from './move.type';

export type CsvData = {
	character: string;
	csvData: Move[];
	csvHeader: string[];
};
