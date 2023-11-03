// Specify the path to your CSV file
const csvFilePath = 'bryan-t8.csv';

// Function to create an expandable area for notes
function createNotesArea(notes) {
    const notesContainer = document.createElement('div');
    notesContainer.className = 'notes-container';
    notesContainer.style.display = 'none'; // Initially hide the notes

    const notesContent = document.createElement('p');
    notesContent.textContent = notes;

    notesContainer.appendChild(notesContent);

    return notesContainer;
}

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
                th.classList.add(prop);
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
                        if (propsRow[j] === 'notes') {
                            const notesButton = document.createElement('div');
                            notesButton.className = 'notes-button';
                            cell.appendChild(notesButton);
                            cell.appendChild(createNotesArea(row[propsRow[j]]));

                            // Add an event listener to toggle the visibility of notes and change the arrow style
                            notesButton.addEventListener('click', function () {
                                const notesContainer = cell.querySelector('.notes-container');
                                if (notesContainer.style.display === 'none') {
                                    notesContainer.style.display = 'block';
                                    notesButton.classList.add('expanded');
                                } else {
                                    notesContainer.style.display = 'none';
                                    notesButton.classList.remove('expanded');
                                }
                            });
                            cell.classList.add(propsRow[j]);
                        } else {
                            cell.textContent = row[propsRow[j]];
                            cell.classList.add(propsRow[j]);
                        }
                    }
                }
            }
        })
        .catch(error => console.error('Error loading CSV file:', error));
}

// Call the function to load the CSV file when the page loads
loadCsvFile();
