/**
 * Created by geoffc on 8/14/14.
 */


var hackDirectives = angular.module('hackDirectives', []);

hackDirectives.directive('messageModal', function() {
    return {
        restrict: 'E',
        templateUrl: 'views/templates/message-modal.html'
    }

});