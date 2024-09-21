document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  console.log(e.submitter.id);
  if ((e.submitter.id == "login")) {
    try {
      console.log("Entre en login")  
      const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (response.ok) {
        alert("Usuario validado");
        // Redirect or update UI as needed
      } else {
        alert(`Error de Inicio de Sesión: ${data.detail}`);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Ocurrio un error intentelo de nuevo");
    }
  } else {
    try {
      console.log("Entre en register")  
      const response = await fetch("http://localhost:8000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (response.ok) {
        alert("Registro realizado");
        // Redirect or update UI as needed
      } else {
        alert(`Error de registro: ${data.detail}`);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Ocurrio un error intentelo de nuevo");
    }
  }
});
