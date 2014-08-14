/**
 * Created by geoffc on 8/13/14.
 */
var hackFilters = angular.module('hackFilters', []);

hackFilters.filter('joinTags', function () {
    return function (input, delimiter) {
        if (input === undefined) {
            return '';
        }
        input = input.map(function (x) {
            return x.text
        });
        return (input || []).join(delimiter || ',');
    };
});