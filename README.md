# Descend Us

Welcome to Descend Us, the [Among Us](https://en.wikipedia.org/wiki/Among_Us) spinoff!


## About the game

Now that you've been [ejected from the spaceship](https://en.wikipedia.org/wiki/Among_Us#Gameplay), you must use your parachute to descend back down to Earth.

The catch is: there's asteroids in the way!

You must navigate and dodge the asteroids. You are also given a laser gun to shoot down the asteroids!

You start being 1000km away from Earth, with 100HP and 10 lasers.

Every time you shoot down an asteroid, you get 50km to reaching Earth.

If you just avoid the asteroids without shooting them, you descend at a rate of 1km/sec.

If you get hit by an asteroid, you lose 5HP.

You must grab the laser packs to replenish your laser supply.


## How to run:

1. [Install requirements](https://pip.pypa.io/en/stable/cli/pip_install/#install-requirement)

```bash
pip install -r requirements.txt
```

2. Invoke Descend Us [as a module](https://docs.python.org/3/using/cmdline.html#cmdoption-m)

```bash
python -m DescendUs
```


## Development

### Write-up

I think this project deserves a level 4+ because it meets all goals of the assignment,
and implements more features (both game-wise and programming-wise) than necessary.

Descend Us is an asteroid avoidance game, however it is more than just that. It adds the 
ability to shoot down asteroids, along with extra lore to engage the user. Not only does adding
extra features (see **Features** section below for details) enhances the game player-wise,
it demonstrates the ability of more programming concepts. This includes implementing the ability
all objects in the game to interact together (eg. `Collidable [Asteroid, Ammo]`, `Laser`), using
abstract classes to represent similar objects (`Collidable` -> `Asteroid`, `Ammo`), and separating
game state (`_globals`, always consistent) from the game itself (other classes, rendered per frame).

Descend Us demonstrates knowledge of lists, functions, and library usage. All game state data
is stored in a globals file ([`DescendUs._globals.py`](./DescendUs/_globals.py)), allowing a
bridge for each process of the game to interact with each other safely. The PyGame library is
used extensively, by implementing concepts learned in class (eg. game state, rendering, colours,
collisions), as well as new concepts from the PyGame documentation (eg. loading audio, loading
images, manipulating/transforming images & surfaces). Descend Us also uses an object oriented
approach (see [`DescendUs.objects`](./DescendUs/objects)) to keep code organized with a clear
and concise logic, as well as following the DRY (don't repeat yourself) principle.

Descend Us' internal documentation includes a program header, clean and readable comments following
[Python's style guide](https://peps.python.org/pep-0008/), understandable variable names, as
well as general code organization and readbility. Regular commits were used to show step-by-step
progress in the development process. Branches and pull requests were used to separate features
and versions of the game. The game is bug-free (when tested on Mac), the code is efficient,
and the game implements elements of randomness (eg. asteroid/ammo generation).

New commands and capabilities of PyGame were implemented into Descend Us. Some listed above were
loading audio, loading and displaying images, transforming (rotating, scaling) images/surfaces.
Though PyGame provides an easy out-of-the-box way to use commands, DescendUs abstracts this
such as through methods (eg. [view](./DescendUs/views) methods, [object](./DescendUs/objects/)
methods) that provide a safe and simple way for each component of the game to interact with.

The sections below will provide insight into the use of mockups and feature lists, and as to
how the planning process of Descend Us went:


### Features

Features are defined in the [version guide](./CHANGELOG.md).

### Resources

Mockups of the UI are available [here](./mockups/).

The version guide is available [here](./CHANGELOG.md).

### Workflow

Each version will be worked on in its own branch. When completed, it will be merged to the `dev` branch. When a full release is available, it will be merged to the `main` branch.