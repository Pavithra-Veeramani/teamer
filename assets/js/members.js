const members = 
[
    {
        id:1,
        name:'Jagadish',
        email: 'jagadish_june17'
    },
    {
        id:2,
        name:'Jagadish2',
        email: 'Joinjiji'
    },
    {
        id:3,
        name: 'Pavithra',
        email: 'pavithra_veeramani'
    },
]


window.addEventListener("load", function(event) {
    let team = document.getElementById("players-list");

    for(let i =0; i < members.length; i++) {
        let row = document.createElement("tr");
        let cell1 = document.createElement("td");
        cell1.innerHTML = members[i].name;
        row.appendChild(cell1);
        let cell2 = document.createElement("td");
        cell2.innerHTML = members[i].email;
        row.appendChild(cell2);
        team.appendChild(row);
    }
}) 
