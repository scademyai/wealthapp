import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-stock-card',
  templateUrl: './stock-card.component.html',
  styleUrls: ['./stock-card.component.scss']
})
export class StockCardComponent {
  @Input() ticker!: string;
  @Input() price!: string;
  @Input() myPortfolio: boolean = false ;

}
