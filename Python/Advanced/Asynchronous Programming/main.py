#!/usr/bin/env python3
# importing asyncio module
import asyncio

# async keyword for async function
async def main():

  # if main program has idle time then run other_function as well specify in task variable
  task = asyncio.create_task(other_function())

  print('A')
  await asyncio.sleep(5) # in this time other_function execute first statement and sleep for 2 secnods for futher

  print('B') # after other_function execute first statment the this will run because other_function is sleeping for 2 seconds
  returned_value = await task # wait until other_function() return 10 value
  print(returned_value)

async def other_function():
  print("1")

  await asyncio.sleep(2) # sleep for 2 seconds

  print("2")
  return 10

# run main() function using asyncio.run(...)
asyncio.run(main())


# await keyword is use to wait/sleep the next execution of further statements
# specify time in seconds in parenthesis
# wait for 1 second then execute next print() function
# await asyncio.sleep(1)
# await other_function()
