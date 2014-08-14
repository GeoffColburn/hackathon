/**
 * Created by geoffc on 8/14/14.
 */


var hackDirectives = angular.module('hackDirectives', []);

hackDirectives.directive('messageModal', function() {
    return {
        restrict: 'E',
        templateUrl: 'views/templates/message-modal.html',
        scope: {
            toUser: '=toUser'
        },
        link: function(scope, element, attr) {
            scope.dismiss = function() {
                $('#messageModal').modal('hide');
            }
        }
    }

});

hackDirectives.directive('inbox', function() {
    return {
        restrict: 'E',
        template: '<a>Inbox ({{unreadMessages.unread}})</a>',
        scope: {
            unreadMessages: '=unreadMessages'
        }
    }
})