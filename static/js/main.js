function darkmode() {
	const wasDarkmode = localStorage.getItem('darkmode') === 'true';
	localStorage.setItem('darkmode', !wasDarkmode);
	const element = document.body;
	element.classList.toggle('dark-mode', !wasDarkmode);

	const logo = document.getElementById('logo');
	if (!wasDarkmode) {
		if (window.location.pathname === '/') {
			logo.setAttribute('src', '/static/images/logo-dark.png');
		}
		const switchInput = document.querySelector('#switch input');
		switchInput.checked = false;
	} else {
		if (window.location.pathname === '/') {
			logo.setAttribute('src', '/static/images/logo.png');
		}
		const switchInput = document.querySelector('#switch input');
		switchInput.checked = true;
	}
}

function onload() {
	console.log('Page: ' + window.location.pathname + ' loaded');
	document.body.classList.toggle(
		'dark-mode',
		localStorage.getItem('darkmode') === 'true'
	);
	const logo = document.getElementById('logo');
	if (localStorage.getItem('darkmode') === 'true') {
		if (window.location.pathname === '/') {
			logo.setAttribute('src', '/static/images/logo-dark.png');
		}
		const switchInput = document.querySelector('#switch input');
		switchInput.checked = false;
	} else {
		if (window.location.pathname === '/') {
			logo.setAttribute('src', '/static/images/logo.png');
		}
		const switchInput = document.querySelector('#switch input');
		switchInput.checked = true;
	}
}
