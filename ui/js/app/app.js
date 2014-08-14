/**
 * Created by Geoff on 8/9/14.
 */
var hackApp = angular.module('hackApp', [
    'ngRoute',
    'ngCookies',
    'ngTagsInput',
    'hackControllers',
    'hackServices',
    'hackFilters',
    'hackDirectives'
]);

hackApp.run(function($rootScope, $location) {
    $rootScope.location = $location;
});


hackApp.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/test/:id', {
            templateUrl: function (urlattr) {
                return 'views/test/' + urlattr.name + '.html';
            }
        })
        .when('/profile/:id', {
            templateUrl: function (urlattr) {
                return 'views/profile.html';
            }
        })
        .when('/projects/:name', {
            templateUrl: function (urlattr) {
                return 'views/projects/' + urlattr.name + '.html';
            }
        })
        .when('/:name', {
            templateUrl: function (urlattr) {
                return 'views/' + urlattr.name + '.html';
            }
        })
        .otherwise({
            redirectTo: 'home'
        })

}]);
