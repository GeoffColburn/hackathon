/**
 * Created by Geoff on 8/9/14.
 */
var hackServices = angular.module('hackServices', ['ngResource']);

hackServices.service('Todo', ['$resource', function($resource) {
    return $resource('api/resources/todo/:id', { id: '@_id' });
}])

hackServices.service('User', ['$resource', function($resource) {
    return $resource('api/resources/user/:id', { id: '@_id' });
}])

hackServices.service('Project', ['$resource', function($resource) {
    return $resource('api/resources/project/:id', { id: '@_id' });
}])

hackServices.service('PrivateMessage', ['$resource', function($resource) {
    return $resource('api/resources/message/:id', { id: '@_id' });
}])