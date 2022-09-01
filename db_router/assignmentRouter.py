class AssignmentRouter:
    route_app_labels = {'assignment'}
    db_name = 'assignment_db'

    def db_for_read(self, model, **hints):
        """
        Attempts to read logs and others models go to assignment_db.
        """
        if model._meta.app_label in self.route_app_labels:
            print("\n\ndb_for_read ::{}\n".format(model._meta.app_label))
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write logs and others models go to assignment_db.
        """
        if model._meta.app_label in self.route_app_labels:
            print("\n\ndb_for_write ::{}\n".format(model._meta.app_label))
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the obj1 or obj2 apps is
        involved.
        """
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            print("\n\nobj1 ::{}//obj2 :: {}\n".format(obj1._meta.app_label, obj2._meta.app_label))
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'assignment_db' database.
        """
        if app_label in self.route_app_labels:
            print("\n\nallow_migrate ::{}\n".format(app_label))
            return self.db_name
        return None