#!/usr/bin/node

document.addEventListener("DOMContentLoaded", () => {
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
        .then(res => res.json())
        .then(data => document.getElementById('hello').textContent = data.hello);
})