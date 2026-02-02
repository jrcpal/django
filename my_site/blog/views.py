from datetime import date
from django.shortcuts import render

all_posts = [
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Jess",
    "date": date(2026, 1, 21),
    "title": "Hiking",
    "excerpt": "It's just like a walking simulator",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
  },
  {
    "slug": "programming-is-fun",
    "image": "coding.jpg",
    "author": "Jess",
    "date": date(2022, 3, 10),
    "title": "Programming Is Great!",
    "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
    "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
      """
    },
    {
      "slug": "into-the-woods",
      "image": "woods.jpg",
      "author": "Jess",
      "date": date(2020, 8, 5),
      "title": "Nature At Its Best",
      "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
      "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
      """
    }
]

def get_date(post):
  return post.get('date')

# Create your views here.

def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, "blog/index.html", {
    "posts": latest_posts
  })

def posts(request):
  return render(request, "blog/all-posts.html", {
    "all_posts": all_posts
  })

def post_detail(request, slug):
  identified_post = next(post for post in all_posts if post['slug'] == slug)
  return render(request, "blog/post-detail.html", {
    "post": identified_post
  })