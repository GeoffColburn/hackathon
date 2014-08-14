/**
 * Created by geoffc on 8/13/14.
 */
var hackFilters = angular.module('hackFilters', []);

hackFilters.filter('joinTags', function () {
    return function (input, delimiter) {
        input = input.map(function (x) {
            return x.text
        });
        return (input || []).join(delimiter || ',');
    };
});