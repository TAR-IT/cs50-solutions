const form = document.getElementById('entry-form');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(form);

  try {
    const response = await fetch('/create_entry/', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      // Update the page with the new entry without a full refresh.
      // You can use response data to update the DOM as needed.
    } else {
      console.error('Failed to create the entry.');
    }
  } catch (error) {
    console.error('Error:', error);
  }
});
