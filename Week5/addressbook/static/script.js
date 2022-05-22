async function getContactsData() {
    const response = await fetch("http://127.0.0.1:5000/");
    return await response.json();
};

function displayContacts() {
    getContactsData()
    .then((contactData) => {
        console.log(contactData);
        postContactData(contactData);
    });
};

function postContactData(contactData) {
    container = document.querySelector(".rolodex");
    for (i = 0; i < contactData.length; i++) {
        const newDiv = document.createElement("div");
        newDiv.className = "card";
        newDiv.innerHTML += `<div class='photo'>${contactData[i].photo}</div>`;
        newDiv.innerHTML += `<div class='name'>${contactData[i].fname}${contactData[i].lname}</div>`;
        newDiv.innerHTML += `<div class='phone'>${contactData[i].number}</div>`;
        newDiv.innerHTML += `<div class='email'>${contactData[i].email}</div>`;
        container.appendChild(newDiv);
    };
};

displayContacts();