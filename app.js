window.onload = () => {


  const div = document.querySelector("#root")
  fetch("http://localhost:9292/random_poe")
  .then( resp => resp.json())
  .then( body => {
    div.innerHTML = JSON.stringify(body)
  })
}