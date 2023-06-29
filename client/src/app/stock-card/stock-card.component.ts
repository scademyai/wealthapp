import { Component, Input } from '@angular/core';
import { HttpService } from '../http.service';
import { AppService } from '../app.service';

@Component({
  selector: 'app-stock-card',
  templateUrl: './stock-card.component.html',
  styleUrls: ['./stock-card.component.scss']
})
export class StockCardComponent {
  @Input() ticker!: string;
  @Input() price!: string;
  @Input() quantity: string= '';
  myPortfolio: boolean = false;
  @Input() parent: string = '';

  constructor(private http: HttpService, private appService: AppService) {
    
  }

  ngOnInit(): void {
    this.myPortfolio = this.isAddedToPortfolio();
  }

  addToPortfolio() {
    this.http.post('/api/portfolio/', { ticker: this.ticker }).subscribe(() => {
      this.myPortfolio = true;
    });
  }

  removeFromPortfolio() {
    this.http.delete(`/api/portfolio/${this.ticker}/`).subscribe(() => {
      this.myPortfolio = false;
      window.location.reload();
    });
  }

  updateQuantity(diff: number) {
    if (this.quantity == '1' && diff == -1) {
      this.removeFromPortfolio();
    }
    else {
      this.http.put(`/api/portfolio/${this.ticker}/`, { diff: diff }).subscribe(() => {
        window.location.reload();
      });
    }
  }
  isAddedToPortfolio(): boolean {
    return this.appService.savedStocksInPortfolio.includes(this.ticker);
  }
}
