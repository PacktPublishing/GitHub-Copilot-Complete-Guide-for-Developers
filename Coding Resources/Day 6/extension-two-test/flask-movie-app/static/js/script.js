document.addEventListener('DOMContentLoaded', function() {
    fetch('/movies/titles')
        .then(response => response.json())
        .then(data => {
            const movieList = document.getElementById('movie-list');
            movieList.innerHTML = '';

            data.titles.forEach(title => {
                const listItem = document.createElement('li');
                listItem.textContent = title;
                movieList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching movie titles:', error));
});