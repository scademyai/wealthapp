import { Component } from '@angular/core';
import { Stock } from '../model';
import { HttpService } from '../http.service';
import { catchError } from 'rxjs/operators';
import { throwError, take } from 'rxjs';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { AppService } from '../app.service';
@Component({
  selector: 'app-my-portfolio',
  templateUrl: './my-portfolio.component.html',
  styleUrls: ['./my-portfolio.component.scss']
})
export class MyPortfolioComponent {
  constructor(private http: HttpService, private appService: AppService
  ) {}

  ngOnInit(): void {
    this.getStocks();
  }

  stocks: Stock[] = [];
  totalOfStocks: number = 0;

  getStocks(): void {
    this.http.get<Stock[]>(`/api/portfolio/`).pipe(
      take(1),
      catchError((error: HttpErrorResponse) => {
        if (error.status === 400) {
          this.stocks = [];
        }
        return throwError(() => new Error(error.message));
      })
    ).subscribe({
      next: (res: Stock[]) => {
        this.stocks = res;
        this.totalOfStocks = this.sumOfMyStocks();
        const tickerNames = res.map(stock => stock.ticker);
        this.appService.savedStocksInPortfolio = tickerNames;
      },
      error: (error: any) => {
        console.error('Error:', error);
      }
    });
  }

  sumOfMyStocks(): number {
    const total = this.stocks.reduce((sum, stock) => sum + Number(stock.price) * Number(stock.quantity), 0);
    return Number(total.toFixed(2));
  }  
}
