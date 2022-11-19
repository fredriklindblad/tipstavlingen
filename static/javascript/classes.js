class Player {
    constructur(name, price, points) {
        this.name = name;
        this.price = price;
        this.points = points;
    }
    get points() {
        return this.name;
    }
}

let myPlayer = new Player('lindblad', 6.5, 60);
console.log(myPlayer.points)