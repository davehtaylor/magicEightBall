// A Magic Eight Ball program that gives the user a random answer from a list
// of responses from an actual Magic Eight Ball


#include <iostream>
#include <string>
#include <chrono> //std::chrono::seconds()
#include <thread> //std::this_thread::sleep_for()
#include <random> //std::default_random_engine()
                  //std::uniform_int_distribution


//Give some pause to appear to be thinking about the answer
void thinking()
{
    int i = 1;

    std::cout << "Contemplating ";

    while (i <= 3)
    {
        // Print three dots, slowly. Wait one second between printing each
        std::cout << '.';
        std::cout.flush();
        std::this_thread::sleep_for(std::chrono::seconds(1));
        i++;
    }
}


int main()
{
    std::string stars(26, '*');
    std::string spaces(5, ' ');

    unsigned int seed = 
        std::chrono::system_clock::now().time_since_epoch().count();
    std::default_random_engine rand_generator;
    rand_generator.seed(seed);
    std::uniform_int_distribution<int> response_range(0,19);
    int rand_index = response_range(rand_generator);

    std::string responses[] {"It is certain",
                             "It is decidedly so",
                             "Without a doubt",
                             "Yes definitely",
                             "You may rely on it",
                             "As I see it, yes",
                             "Most likely",
                             "Outlook good",
                             "Yes",
                             "Signs point to yes",
                             "Reply hazy try again",
                             "Ask again later",
                             "Better not tell you now",
                             "Cannot predict now",
                             "Concentrate and ask again",
                             "Don't count on it",
                             "My reply is no",
                             "My sources say no",
                             "Outlook not so good",
                             "Very doubtful"};
  
    // Print a pretty banner
    std::cout << std::endl;
    std::cout << stars << std::endl;
    std::cout << spaces;
    std::cout << "MAGIC EIGHT BALL";
    std::cout << spaces << std::endl;
    std::cout << stars << std::endl;

    std::cout << std::endl;

    std::cout << "Think long and hard about your question. \n"
        "When you are ready, press the enter key\n"
        "to recieve your answer." << std::endl;

    // Wait for the user to press enter
    std::getchar();

    thinking();
    std::cout << std::endl;

    std::cout << responses[rand_index] << std::endl;
    std::cout << std::endl;

    return 0;
}
