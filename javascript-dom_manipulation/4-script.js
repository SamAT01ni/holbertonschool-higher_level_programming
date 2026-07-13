#!/usr/bin/node

document.getElementById('add_item').addEventListener('click', () => {
    const ul = document.getElementById("my_list");
    const li = document.createElement('li');
    li.textContent = 'Item';
    document.querySelector('ul').appendChild(li);
});