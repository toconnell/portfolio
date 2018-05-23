var app = angular.module('portfolio', []);

app.controller('bodyController', function($scope, $http) {

	$scope.scratch = {
		currentView: 'portfolio.html',
	};

	// 'imports' from modular JS
	$scope.socialLinks = socialLinks;	// imported into $scope by HTML template

	var postsPromise = $http({method: 'GET', url: 'https://api.toconnell.info/posts/0'})
	postsPromise.then(function successCallback(response) {
		$scope.posts = response.data;
  	}, function errorCallback(response) {
		console.error("Coult not retrieve posts!");
    });

	$scope.newTab = function(url) {
		window.open(url);
	};

});

