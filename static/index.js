const form = document.getElementById('myForm');
const responseContainer = document.getElementById('responseContainer');
const imageResponse = document.getElementById('imageResponse');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  // Retrieve the form data
  const formData = new FormData(form);
  const formValues = Object.fromEntries(formData.entries());

  // Send a POST request to the server
  fetch('/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(formValues)
  })
  .then(response => response.blob())
  .then(blob => {
    // Create a local URL for the image blob
    const imageUrl = URL.createObjectURL(blob);

    // Hide the form
    form.classList.add('hidden');

    // Show the image response
    responseContainer.classList.remove('hidden');
    imageResponse.src = imageUrl;
  })
  .catch(error => console.error(error));
});

