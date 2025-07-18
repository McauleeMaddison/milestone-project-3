document.addEventListener('DOMContentLoaded', () => {
  const addFieldButton = document.getElementById('add-field');
  const additionalFieldsContainer = document.getElementById('additional-fields');
  let fieldCount = 1; // Start counting from 1

  // Add new input field on button click
  addFieldButton.addEventListener('click', () => {
    fieldCount++;
    const newField = document.createElement('div');
    newField.classList.add('input-group');
    newField.innerHTML = `
      <label for="field${fieldCount}">Field ${fieldCount}:</label>
      <input type="text" id="field${fieldCount}" name="field${fieldCount}" placeholder="Enter data for Field ${fieldCount}">
    `;
    additionalFieldsContainer.appendChild(newField);
  });
});
