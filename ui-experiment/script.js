// Specify the path to your CSV file
const csvFilePath = 'bryan-t8.csv';

// Function to load the CSV file
function loadCsvFile() {
    fetch(csvFilePath)
        .then(response => response.text())
        .then(data => {
            const table = document.getElementById('table');
            table.innerHTML = ''; // Clear previous data

            const result = Papa.parse(data, {
                header: true,
                dynamicTyping: true
            });
            const propsRow = result.meta.fields;
            const rows = result.data;
            console.log(rows);

            // Add table headers
            const headerRow = table.createTHead();
            propsRow.forEach((prop) => {
                const th = document.createElement('th');
                th.textContent = prop;
                headerRow.appendChild(th);
            });

            for (let i = 0; i < rows.length; i++) {
                const row = rows[i];
                if (row) {
                    // Create a new row in the table
                    const newRow = table.insertRow();

                    for (let j = 0; j < propsRow.length; j++) {
                        // Add cells to the row
                        const cell = newRow.insertCell(j);
                        cell.textContent = row[propsRow[j]];
                        cell.classList.add(propsRow[j]);
                    }
                }
            }
        })
        .catch(error => console.error('Error loading CSV file:', error));
}

// Call the function to load the CSV file when the page loads
loadCsvFile();
