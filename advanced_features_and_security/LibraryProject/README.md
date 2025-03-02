# LibraryProject - Permissions & Groups

## Overview
This project implements user permissions and groups to control access to various parts of the Django application. It ensures that different user roles have appropriate access levels for managing books and other resources.

## Permissions Setup
Custom permissions were added to the `Book` model to restrict actions based on user roles.

### Custom Permissions Defined in `models.py`
- `can_view`: Allows a user to view book records.
- `can_create`: Allows a user to add new books.
- `can_edit`: Allows a user to modify existing books.
- `can_delete`: Allows a user to delete books.

## Groups & Role-Based Access Control
Three user groups were created to manage permissions effectively:
- **Admins**: Full access to all operations (view, create, edit, delete).
- **Editors**: Can view, create, and edit books but cannot delete them.
- **Viewers**: Can only view books.

### Group Setup in `admin.py`
- Groups were created via the Django Admin panel.
- Permissions were assigned to each group accordingly.

## Enforcing Permissions in Views
In `views.py`, permission decorators were used to enforce access control:
- `@permission_required('bookshelf.can_edit', raise_exception=True)`: Ensures only users with edit permissions can modify book entries.
- `@permission_required('bookshelf.can_delete', raise_exception=True)`: Restricts deletion access to users with delete permissions.
- Function-based and class-based views were updated to check permissions before executing actions.

## Testing Permissions
To test the implementation:
1. Create test users and assign them to different groups via the Django Admin panel.
2. Log in as each user and verify their ability to perform allowed and restricted actions.
3. Attempt accessing unauthorized actions and confirm proper access denial messages.

## Folder Structure
```
LibraryProject/
│── bookshelf/
│   │── migrations/
│   │── templates/
│   │── views.py
│   │── models.py
│   │── forms.py
│── LibraryProject/
│   │── settings.py
│── README.md  # This file
```

## Notes
- Users can be assigned to groups via the Django Admin panel.
- Groups and permissions can be modified dynamically using the Django shell or Admin panel.
- Ensure that permissions are correctly applied when adding new features.

