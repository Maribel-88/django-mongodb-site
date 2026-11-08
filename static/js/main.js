document.getElementById('registrationForm').addEventListener('submit',async function(event){
  event.preventDefault(); //Stop standard form reload behavior 

  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const responseMessage = document.getElementById('responseMessage');

  try {
    //Send our POST request straight to Django's endpoint route
    const response = await fetch('/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, email: email})
    });

    const result = await response.json();

    if (response.ok) {
        responseMessage.innerText = result.message;
        responseMessage.style.color = "green";
        document.getElementById('registrationForm'.reset);
    } else {
        responseMessage.innerText = result.error || "An error occured.";
        responseMessage.style.color = "red";
    }
  } catch (error) {
    console.error("Communication error:", error);
    responseMessage.innerText = "Could not establish connection to the server.";
    responseMessage.style.color = "red";
  }
});