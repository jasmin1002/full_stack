// Define a generic Person class
class Person {
    constructor(firstname='firstname', lastname='lastname', middlename='middlename', country='country', height=0.0) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.middlename = middlename;
        this.country = country;
        this.height = height;
    }
}

// Instantiate mySelf object
const mySelf = new Person('Sikiru', 'JIMOH', 'Olalekan', 'Nigeria', 6.78)

// Select output holder tag
const container = document.querySelector('.container');

// Destructure mySelf object
const {lastname, firstname, middlename, country, height} = mySelf;

// Wrap the values with appropriate html tags
container.children[0].textContent = `Name: ${lastname} ${firstname} ${middlename}`;
container.children[1].textContent = `Height: ${height}cm`
container.children[2].textContent = `Country: ${country}`
