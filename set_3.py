{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e829b794-0f2a-41f6-be70-124cdd7ed623",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after function definition on line 41 (1442474825.py, line 43)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[1], line 43\u001b[1;36m\u001b[0m\n\u001b[1;33m    fromfollowto = to_member in social_graph[from_member][\"following\"]\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block after function definition on line 41\n"
     ]
    }
   ],
   "source": [
    "'''Programming Set 3\n",
    "\n",
    "This assignment will develop your ability to manipulate data.\n",
    "'''\n",
    "\n",
    "def relationship_status(from_member, to_member, social_graph):\n",
    "    '''Relationship Status.\n",
    "\n",
    "    Let us pretend that you are building a new app.\n",
    "    Your app supports social media functionality, which means that users can have\n",
    "    relationships with other users.\n",
    "\n",
    "    There are two guidelines for describing relationships on this social media app:\n",
    "    1. Any user can follow any other user.\n",
    "    2. If two users follow each other, they are considered friends.\n",
    "\n",
    "    This function describes the relationship that two users have with each other.\n",
    "\n",
    "    Please see \"set_3_sample_data.py\" for sample data. The social graph\n",
    "    will adhere to the same pattern.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    from_member: str\n",
    "        the subject member\n",
    "    to_member: str\n",
    "        the object member\n",
    "    social_graph: dict\n",
    "        the relationship data\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        \"follower\" if from_member follows to_member,\n",
    "        \"followed by\" if from_member is followed by to_member,\n",
    "        \"friends\" if from_member and to_member follow each other,\n",
    "        \"no relationship\" if neither from_member nor to_member follow each other.\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    def relationship_status(from_member, to_member, social_graph):\n",
    "    # i dont have wifi at home rn im working off mobile data and a dream\n",
    "    fromfollowto = to_member in social_graph[from_member][\"following\"]\n",
    "    tofollowfrom = from_member in social_graph[to_member][\"following\"]\n",
    "    \n",
    "    if fromfollowto and tofollowfrom:\n",
    "        return \"friends\"\n",
    "    elif fromfollowto:\n",
    "        return \"follower\"\n",
    "    elif tofollowfrom:\n",
    "        return \"followed by\"\n",
    "    else:\n",
    "        return \"no relationship\"\n",
    "\n",
    "\n",
    "def tic_tac_toe(board):\n",
    "    '''Tic Tac Toe.\n",
    "\n",
    "    Tic Tac Toe is a common paper-and-pencil game.\n",
    "    Players must attempt to successfully draw a straight line of their symbol across a grid.\n",
    "    The player that does this first is considered the winner.\n",
    "\n",
    "    This function evaluates a tic tac toe board and returns the winner.\n",
    "\n",
    "    Please see \"set_3_sample_data.py\" for sample data. The board will adhere\n",
    "    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never\n",
    "    have more than one winner. The board will only ever have 2 unique symbols at the same time.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    board: list\n",
    "        the representation of the tic-tac-toe board as a square list of lists\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the symbol of the winner or \"NO WINNER\" if there is no winner\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    def tic_tac_toe(board):\n",
    "    #literaly the most important line in the code lmao\n",
    "    size = len(board)\n",
    "    #checks the boring ways to win tic tac toe\n",
    "    for row in board:\n",
    "        if row.count(row[0]) == size and row[0] != '':\n",
    "            return row[0]\n",
    "    for col in range(size):\n",
    "        column = [board[row][col] for row in range(size)]\n",
    "        if column.count(column[0]) == size and column[0] != '':\n",
    "            return column[0]\n",
    "    #checks the way funnier but far unlikelier ways to win tic tac toe\n",
    "    diagonal = [board[i][i] for i in range(size)]\n",
    "    if diagonal.count(diagonal[0]) == size and diagonal[0] != '':\n",
    "        return diagonal[0]\n",
    "    anti_diagonal = [board[i][size - 1 - i] for i in range(size)]\n",
    "    if anti_diagonal.count(anti_diagonal[0]) == size and anti_diagonal[0] != '':\n",
    "        return anti_diagonal[0]\n",
    "    #did you know its impossible to lose at tic tac toe if you know what you're doing\n",
    "    return \"NO WINNER\"\n",
    "\n",
    "def eta(first_stop, second_stop, route_map):\n",
    "    '''ETA.\n",
    "\n",
    "    A shuttle van service is tasked to travel along a predefined circlar route.\n",
    "    This route is divided into several legs between stops.\n",
    "    The route is one-way only, and it is fully connected to itself.\n",
    "\n",
    "    This function returns how long it will take the shuttle to arrive at a stop\n",
    "    after leaving another stop.\n",
    "\n",
    "    Please see \"set_3_sample_data.py\" for sample data. The route map will\n",
    "    adhere to the same pattern. The route map may contain more legs and more stops,\n",
    "    but it will always be one-way and fully enclosed.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    first_stop: str\n",
    "        the stop that the shuttle will leave\n",
    "    second_stop: str\n",
    "        the stop that the shuttle will arrive at\n",
    "    route_map: dict\n",
    "        the data describing the routes\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the time it will take the shuttle to travel from first_stop to second_stop\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    def eta(first_stop, second_stop, route_map):\n",
    "    total_time = 0\n",
    "    stop = first_stop\n",
    "\n",
    "    #because overshooting our destination would SUCK\n",
    "    while stop != second_stop:\n",
    "        # had to google what a tuple was\n",
    "        for (start, end), data in route_map.items():\n",
    "            if start == stop:\n",
    "                travel_time = data['travel_time_mins']\n",
    "                total_time += travel_time\n",
    "                stop = end\n",
    "                break\n",
    "\n",
    "\n",
    "    return total_time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62593872-8adf-44b7-ab89-34a923b40d05",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
