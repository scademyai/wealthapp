import { Component } from '@angular/core';
import { Stock } from '../model';
@Component({
  selector: 'app-my-portfolio',
  templateUrl: './my-portfolio.component.html',
  styleUrls: ['./my-portfolio.component.scss']
})
export class MyPortfolioComponent {

  stocks: Stock[] = [
    {
      "ticker": "TSLA",
      "price": "270.00",
      "volume": "1000000"
  },
  {
      "ticker": "AAPL",
      "price": "200.00",
      "volume": "2000000"
  },
  {
      "ticker": "GOOG",
      "price": "1000.00",
      "volume": "3000000"
  }
  ];
}
