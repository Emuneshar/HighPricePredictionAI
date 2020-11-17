using System;
using System.IO;
using IronPython.Hosting;

namespace HighPricePredictionAI.Data
{
    public class WebScraper
    {
        public static void Scraper()
        {
            var engine = Python.CreateEngine();
            var source = engine.CreateScriptSourceFromFile(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Scraper.py");
            var scope = engine.CreateScope();
            
            source.Execute(scope);

            var scraper = scope.GetVariable("Ticker");
            var instance = engine.Operations.CreateInstance(scraper);

            Console.WriteLine(instance.scrape());
        }
    }
}