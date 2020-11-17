using System;
using HighPricePredictionAI.Data;

namespace HighPricePredictionAI
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Data.WebScraper.Scraper();
            }
            catch
            {
                Console.WriteLine("Error Found In Code");
            }
            
        }
    }
}
