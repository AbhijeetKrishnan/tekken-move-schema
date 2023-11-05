import Papa from 'papaparse';

// Specify the path to your CSV file
const csvFilePath = '/bryan-t8.csv';

let csvData: any[] = [];
let csvHeader: string[] | undefined = [];

export async function load({ fetch }) {
    try {
        const response = await fetch(csvFilePath);
        const data = await response.text();

        const result = Papa.parse(data, {
            header: true,
            dynamicTyping: true
        });

        csvData = result.data;
        csvHeader = result.meta.fields;

        return {
            props: {
            data: csvData,
            header: csvHeader,
            },
        };
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}