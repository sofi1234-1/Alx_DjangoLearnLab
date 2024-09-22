# Django Blog Project

## Features

- Create, Read, Update, and Delete (CRUD) functionalities for blog posts.
- Authentication required for creating and managing posts.
- Permissions in place to ensure users can only edit or delete their own posts.

## URLs

- `/` - List all blog posts.
- `/posts/new/` - Form to create a new blog post.
- `/posts/<int:pk>/` - View details of an individual post.
- `/posts/<int:pk>/edit/` - Form to edit an existing post.
- `/posts/<int:pk>/delete/` - Confirm deletion of a post.
