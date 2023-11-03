document.getElementById('csvFile').addEventListener('change', handleFile);

function handleFile(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            const csvData = e.target.result;
            const table = document.getElementById('table');
            table.innerHTML = ''; // Clear previous data

            // Split CSV data into rows
            const rows = csvData.split('\n');

            for (let i = 0; i < rows.length; i++) {
                const row = rows[i].trim();
                if (row) {
                    const cells = row.split(',');

                    // Create a new row in the table
                    const newRow = table.insertRow();

                    for (let j = 0; j < cells.length; j++) {
                        // Add cells to the row
                        const cell = newRow.insertCell(j);
                        cell.textContent = cells[j];

                        // Apply specific classes based on CSV column values
                        if (j === 0) {
                            cell.classList.add('column1-style'); // Add class for the first column
                        } else if (j === 1) {
                            cell.classList.add('column2-style'); // Add class for the second column
                        }

                        // You can add more conditions to apply classes to other columns as needed
                    }
                }
            }
        };

        reader.readAsText(file);
    }
}
