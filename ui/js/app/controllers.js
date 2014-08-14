/**
 * Created by Geoff on 8/9/14.
 */
var hackControllers = angular.module('hackControllers', []);


hackControllers.controller('MainController', function ($scope, $http, $location, $cookies, User) {
    var id = $cookies.user;
    $scope.user = User.get({id: id});

    $scope.login = function (user) {
        $http.post('auth/login', user).success(function (data) {
            $scope.user = User.get({id: data._id});
            $location.path('/home')
        });
    };

    $scope.logout = function () {
        $http.get('auth/logout').success(function (data) {
            $scope.user = {
                isLoggedIn: false
            }
        });
    };

});


hackControllers.controller('HomeController', function ($scope) {
});

hackControllers.controller('TestController', function ($scope, $http, $location) {
    $scope.user = {email: 'admin', password: 'test'};
    $scope.login = function () {
        $http.post('auth/login', $scope.user).success(function (data) {
            console.dir(data);
            $location.path('/home')
        });

    }
});


hackControllers.controller('TodoController', function ($scope, Todo) {
    $scope.todo = {};
    $scope.todos = Todo.query();

    $scope.add = function () {
        var todo = new Todo($scope.todo);
        todo.$save(function () {
            $scope.todos = Todo.query();
            $scope.todo = {};
        });

    }

    $scope.remove = function (todo) {
        todo.$remove(function () {
            $scope.todos = Todo.query();
        });
    }

});

hackControllers.controller('ImageUploadController', function ($scope) {
    //http://stackoverflow.com/questions/18571001/file-upload-using-angularjs
});

hackControllers.controller('UserController', function($scope, $routeParams, $cookies, User) {
    var id = $routeParams.id;
    $scope.user = User.get({id: id})

    $scope.isOwner = id === $cookies.user;

    $scope.saveChanges = function() {
        var model = new User($scope.user);
        model.$save();
    }

});

hackControllers.controller('ProjectController', function($scope, $routeParams, $cookies, $location, Project) {
    var id = $routeParams.id;
    if (id !== undefined) {
        $scope.project = Project.get({id: id})
    } else {
        $scope.project = {};
        $scope.project.isEditable = true;
        $scope.project.tags = []
    }

    $scope.saveChanges = function() {
        var model = new Project($scope.project);
        model.$save();
        if ('return_url' in $routeParams){
            $location.path($routeParams.return_url)
        }
    }

    $scope.addRole = function() {
        if ($scope.project.roles === undefined) {
            $scope.project.roles = [];
        }

        $scope.project.roles.push($scope.role);

        var model = new Project($scope.project);
        model.$save();
    }

});

hackControllers.controller('ProjectListController', function($scope, $routeParams, $cookies, Project) {
    console.dir($routeParams)
    $scope.projects = Project.query({user_id: $routeParams.user_id});

});

hackControllers.controller('UserListController', function($scope, User) {
   $scope.users = User.query();
});