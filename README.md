Problem Statement:

One day, Alex got tired of climbing in a gym and decided to take a very large group of climbing friends outside to climb. 
The climbing area where they went had a huge, wide boulder, not very tall, with various marked hand and foot holds. Alex quickly determined an “allowed” set
of moves that her group of friends can perform to get from one hold to another. 
The overall system of holds can be described by a rooted tree $T$ with $n$ vertices, where each vertex corresponds to a hold, and each edge corresponds to an allowed move between holds. 
The climbing paths converge as they go up the boulder, leading to a unique hold at the summit, represented by the root of $T$. 
Alex and her friends (who are all excellent climbers) decided to play a game where as many climbers as possible are simultaneously on the boulder and each climber needs
to perform a sequence of exactly $k$ moves. Each climber can choose an arbitrary hold to start from, and all moves must move away from the ground. 
Thus, each climber traces out a path of $k$ edges in the tree $T$, all directed toward the root. 
However, no two climbers are allowed to touch the same hold; the paths followed by different climbers cannot intersect at all. 

Describe and analyze an efficient dynamic programming algorithm to compute the maximum number of climbers that can play this game.
